"""
Cylinders on a 2D square lattice
"""
import numpy
import bornagain as ba
from bornagain import deg, angstrom, nm


def get_sample():
    """
    Returns a sample with cylinders on a substrate, forming a 2D square lattice.
    """
    # defining materials
    m_vacuum = ba.HomogeneousMaterial("Vacuum", 0.0, 0.0)
    m_substrate = ba.HomogeneousMaterial("Substrate", 6e-6, 2e-8)
    m_particle = ba.HomogeneousMaterial("Particle", 6e-4, 2e-8)

    # collection of particles
    interference = ba.InterferenceFunction2DLattice(
        ba.SquareLattice2D(25.0*nm, 0*deg))
    pdf = ba.FTDecayFunction2DCauchy(48*nm, 16*nm, 0)
    interference.setDecayFunction(pdf)

    cylinder_ff = ba.FormFactorCylinder(3.*nm, 3.*nm)
    cylinder = ba.Particle(m_particle, cylinder_ff)
    particle_layout = ba.ParticleLayout()
    particle_layout.addParticle(cylinder)
    particle_layout.setInterferenceFunction(interference)

    # assembling the sample
    vacuum_layer = ba.Layer(m_vacuum)
    vacuum_layer.addLayout(particle_layout)
    substrate_layer = ba.Layer(m_substrate)

    multi_layer = ba.MultiLayer()
    multi_layer.addLayer(vacuum_layer)
    multi_layer.addLayer(substrate_layer)
    print(multi_layer.parametersToString())
    print(multi_layer.treeToString())
    return multi_layer


def get_simulation():
    """
    Create and return GISAXS simulation with beam and detector defined
    """
    simulation = ba.GISASSimulation()
    simulation.setDetectorParameters(200, -2.0*deg, 2.0*deg, 200, 0.0*deg,
                                     2.0*deg)
    simulation.setBeamParameters(1.0*angstrom, 0.2*deg, 0.0*deg)
    return simulation


def run_simulation():
    """
    Runs simulation and returns intensity map.
    """
    simulation = get_simulation()
    simulation.setSample(get_sample())
    simulation.runSimulation()
    return simulation.result()


if __name__ == '__main__':
    result = run_simulation()
    ba.plot_simulation_result(result, cmap='jet', aspect='auto')
