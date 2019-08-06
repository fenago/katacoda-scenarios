In this step, we will clone and build Libra core.

#### Clone the Libra Core Repository
`git clone https://github.com/libra/libra.git`{{execute}}

#### Install Dependencies
To setup Libra Core, change to the libra directory and run the setup script to install the dependencies, as shown below:

`cd libra && ./scripts/dev_setup.sh`{{execute}}

The above setup script installs the following:

-  rustup — rustup is an installer for the Rust programming language, which Libra Core is implemented in.
-  required versions of the rust-toolchain.
-  CMake — to manage the build process.
-  protoc — a compiler for protocol buffers.
-  Go — for building protocol buffers.