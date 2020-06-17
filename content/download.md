+++
title = "Download"
menu = "main"
weight = 30
breadcrumb = true
+++

<div class="container page-download">
  <div class="row">
    <div class="col-lg-10 mx-auto">
    <h5> Current release {{% release-string %}}</h5>
    <p> View changes made in <a href="{{% last-release-letter %}}">this release</a> </p>
    </div>
  </div>
  <hr class="feature-divider">
  <div class="row">
    <div class="col-lg-10 mx-auto mt-1 mb-5">
    <p class ="text-sm-center font-italic">
      BornAgain is supported under Windows, Mac OS X and Linux operating systems. For Windows and MacOS we provide binary installer packages for Python3, 64-bit. For Unix-like operating systems (including Linux and Mac OS X) we support installation from source.
    </p>
  <hr class="feature-divider">
    <p>Use links below to download the appropriate package. Previous versions are available <a href="{{% download-loc %}} " onclick="ga('send', 'event', 'download', 'click', 'previous-ver');">here<a>.</p>
    </div>
  </div>


<!-- Nav tabs -->
<ul class="nav nav-tabs nav-pills nav-fill " id="OperationSystemTab" role="tablist">
  <li class="nav-item">
    <a class="nav-link" id="home-tab" data-toggle="tab" href="#Windows" role="tab" aria-controls="home" aria-selected="true">Windows</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="profile-tab" data-toggle="tab" href="#MacOS" role="tab" aria-controls="profile" aria-selected="false">MacOS</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="messages-tab" data-toggle="tab" href="#Linux" role="tab" aria-controls="messages" aria-selected="false">Linux</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="messages-tab" data-toggle="tab" href="#Documents" role="tab" aria-controls="messages" aria-selected="false">Documents</a>
  </li>
</ul>

<!-- Tab panes -->
<div class="tab-content" id="OperationSystemTabContent">
  <div class="tab-pane fade" id="Windows" role="tabpanel" aria-labelledby="profile-tab">
    <div class="d-flex flex-column flex-md-row justify-content-center">
      <div class="card text-center bg-light mx-3 my-5 border-primary ba-custom-border" style="width: 18rem;">
        <div class="card-header">Windows, 64-bit (x86)</div>
        <div class="card-body">
          <h5 class="card-title">Windows, Python 3.8</h5>
          <p><span class="badge badge-primary mr-1">Recommended</span></p>
          <p class="card-text">Windows 7,8,10 binary installer intended for Python 3.8</p>
          <a href="{{% ref-installer-win "3.8" %}}" onclick="ga('send', 'event', 'download', 'click', 'win-py37');" class="btn btn-primary ba-custom">Download</a>
        </div>
      </div>
    </div>
  </div>

  <div class="tab-pane fade" id="MacOS" role="tabpanel" aria-labelledby="profile-tab">
    <div class="d-flex flex-column flex-md-row justify-content-center">
      <div class="card text-center bg-light mx-3 my-5 border-primary ba-custom-border" style="width: 22rem;">
        <div class="card-header">MacOS, 64-bit (x86)</div>
        <div class="card-body">
          <h5 class="card-title">MacOS, Python 3.8</h5>
          <p><span class="badge badge-primary mr-1">Recommended</span></p>
          <p class="card-text">MacOS 10.13 (High Sierra), 10.14 (Mojave) and 10.15 (Catalina)</p>
          <a href="{{% ref-installer-mac "3.8" %}}" onclick="ga('send', 'event', 'download', 'click', 'mac-py37')" class="btn btn-primary ba-custom">Download</a>
        </div>
      </div>
    </div>
  </div>

  <div class="tab-pane fade" id="Linux" role="tabpanel" aria-labelledby="messages-tab">
    <div class="d-flex flex-column flex-md-row justify-content-center">
      <div class="card text-center bg-light mx-5 my-5 border-primary ba-custom-border" style="width: 80%;">
        <div class="card-header">Get source code</div>
        <div class="card-body">
          <h5 class="card-title">Clone Git repository</h5>
          <p>
          <pre><code>{{% git-clone %}}</code></pre>
          </p>
          <h5 class="card-title">or</h5>
          <a href="{{% ref-tarball %}}" onclick="ga('send', 'event', 'download', 'click', 'tarball');" class="btn btn-primary ba-custom">Download tarball</a>
        </div>
      </div>
    </div>
  </div>

  <div class="tab-pane fade" id="Documents" role="tabpanel" aria-labelledby="messages-tab">
    <div class="d-flex flex-column flex-md-row justify-content-center">
      <div class="card text-center bg-light mx-3 my-5 border-primary ba-custom-border" style="width: 22rem;">
        <div class="card-header">Reference Paper</div>
        <div class="card-body">
          <h5 class="card-title">J. Appl. Cryst. 2020</h5>
          <a href="{{% ref-paper %}}" onclick="ga('send', 'event', 'download', 'click', 'manual');" class="btn btn-primary ba-custom">Download pdf</a>
        </div>
      </div>
      <div class="card text-center bg-light mx-3 my-5 border-primary ba-custom-border" style="width: 22rem;">
        <div class="card-header">Form Factor Catalog</div>
        <div class="card-body">
          <h5 class="card-title">Catalog</h5>
          <a href="{{% ref-ffcatalog %}}" onclick="ga('send', 'event', 'download', 'click', 'manual');" class="btn btn-primary ba-custom">Download pdf</a>
        </div>
      </div>
      <div class="card text-center bg-light mx-3 my-5 border-primary ba-custom-border" style="width: 22rem;">
        <div class="card-header">Physics Manual (incomplete)</div>
        <div class="card-body">
          <h5 class="card-title">Manual</h5>
          <a href="{{% ref-manual %}}" onclick="ga('send', 'event', 'download', 'click', 'manual');" class="btn btn-primary ba-custom">Download pdf</a>
        </div>
      </div>
    </div>
  </div>

</div>

  <hr class="feature-divider">
  <div class="row">
    <div class="col-lg-10 mx-auto mt-2">
      To use BornAgain from Python you have to have Python interpreter installed.
      See {{< local-link "documentation/getting-started/installation">}} installation instructions {{< /local-link >}}for more details.
    </div>
  </div>

  </div>
