import bornagain as ba
from bornagain import deg, nm, kvector_t

# parameters of 3D particle arrangement
particle_radius = 2.5*nm
lattice_length = 10.0*nm
height = 50.0*nm

# lattice rotations dictionary, consists of pairs "xi: weight"
# sum of the weights must be less or equal to 1
rotations = {0.0: 0.7, 45.0: 0.3}


def get_sample():
    # Defining Materials
    m_air = ba.HomogeneousMaterial("Air", 0.0, 0.0)
    m_particle = ba.HomogeneousMaterial("Particle", 0.0006, 2e-08)
    m_substrate = ba.HomogeneousMaterial("Substrate", 6e-06, 2e-08)

    # Defining Layers
    l_air = ba.Layer(m_air)
    l_substrate = ba.Layer(m_substrate)

    # Defining Form Factors
    ff_sphere = ba.FormFactorFullSphere(particle_radius)

    # Defining composition of particles at specific positions
    particle_composition = ba.ParticleComposition()
    # compute number of particles in the vertical direction
    n = int((height - 2.0*particle_radius) // lattice_length)
    # add particles to the particle composition
    for i in range(n+1):
        particle = ba.Particle(m_particle, ff_sphere)
        particle_position = kvector_t(0.0*nm, 0.0*nm, i*lattice_length)
        particle.setPosition(particle_position)
        particle_composition.addParticle(particle)

    for xi in rotations.keys():
        # Defining Interference Function
        interference = ba.InterferenceFunction2DLattice(lattice_length, lattice_length, 90.0*deg, xi*deg)
        interference_pdf = ba.FTDecayFunction2DCauchy(500.0*nm, 500.0*nm, 0.0*deg)
        interference.setDecayFunction(interference_pdf)

        # Defining Particle Layout and adding Particles
        layout = ba.ParticleLayout()
        layout.addParticle(particle_composition, 1.0)
        layout.setInterferenceFunction(interference)
        layout.setWeight(rotations[xi])

        # Adding layouts to layers
        l_air.addLayout(layout)

    # Defining Multilayers
    multilayer = ba.MultiLayer()
    multilayer.addLayer(l_air)
    multilayer.addLayer(l_substrate)
    return multilayer


def get_simulation():
    simulation = ba.GISASSimulation()
    simulation.setDetectorParameters(400, -2.0*deg, 2.0*deg, 400, 0.0*deg, 3.0*deg)
    
    simulation.setBeamParameters(0.1*nm, 0.2*deg, 0.0*deg)
    simulation.setBeamIntensity(1.0e+08)
    # simulation.getOptions().setMonteCarloIntegration(True, 20)     # if height is large
    return simulation


def run_simulation():
    sample = get_sample()
    simulation = get_simulation()
    simulation.setSample(sample)
    simulation.runSimulation()
    return simulation.result()


if __name__ == '__main__':
    result = run_simulation()
    ba.plot_simulation_result(result, intensity_max=1e+06)
