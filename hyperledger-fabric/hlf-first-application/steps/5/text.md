Now that we have the administrator’s credentials in a wallet, we can enroll a new user "user1" which will be used to query and update the ledger:
`node registerUser.js`{{execute T1}}

Similar to the admin enrollment, this program uses a CSR to enroll user1 and store its credentials alongside those of admin in the wallet. We now have identities for two separate users — admin and user1 — and these are used by our application.

Time to interact with the ledger…
