
When we created the network, an admin user — literally called admin — was created as the registrar for the certificate authority (CA). Our first step is to generate the private key, public key, and X.509 certificate for admin using the enroll.js program. 

This process uses a Certificate Signing Request (CSR) — the private and public key are first generated locally and the public key is then sent to the CA which returns an encoded certificate for use by the application. These three credentials are then stored in the wallet, allowing us to act as an administrator for the CA.

We will subsequently register and enroll a new application user which will be used by our application to interact with the blockchain.

Let’s enroll user admin:
`node enrollAdmin.js`{{execute T1}}

This command has stored the CA administrator’s credentials in the wallet directory.