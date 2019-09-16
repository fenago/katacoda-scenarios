If you are running a distribution that comes with apt, such as Ubuntu or Debian, there's an x86_64 package available for the Azure CLI. This package has been tested with and is supported for:

- **Ubuntu:** trusty, xenial, artful, bionic, and disco

- **Debian:** wheezy, jessie, and stretch

The current version of the Azure CLI is 2.0.x. To find your installed version and see if you need to update, run `az --version`.

**Note:** The package for Azure CLI installs its own Python interpreter, and does not use the system Python.