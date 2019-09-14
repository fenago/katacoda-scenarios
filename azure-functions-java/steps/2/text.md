In this step, we will clone and build Libra core.

#### Clone the Libra Core Repository
`git clone https://github.com/libra/libra.git`{{execute T1}}

#### Checkout the testnet Branch
`cd libra && git checkout testnet`{{execute T1}}

#### Install Dependencies
To install az cli, run the followig command:

`curl -sL https://aka.ms/InstallAzureCLIDeb | bash`{{execute T1}}


In this environment you can check that Java (JRE) is already installed by running `java -version`{{execute T1}}

We can work using maven by running executable command mvn from you shell prompt. Try to run `mvn -version`{{execute T1}} to check whether you have Maven installed in this environment.

If you get output with Maven version information, then Maven is already installed and you are ready to use Maven.