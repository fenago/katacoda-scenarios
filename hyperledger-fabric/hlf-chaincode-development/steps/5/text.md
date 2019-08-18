<pre class="file" data-filename="sacc.go">
// main function starts up the chaincode in the container during instantiate
func main() {
    if err := shim.Start(new(SimpleAsset)); err != nil {
            fmt.Printf("Error starting SimpleAsset chaincode: %s", err)
    }
}
</pre>

Now let’s compile your chaincode.
`go get -u github.com/hyperledger/fabric/core/chaincode/shim`{{execute}}

`go build`{{execute}}

If there are no errors, it means compilation was susccessful. In the upcoming [Chaincode Testing in Dev](https://www.katacoda.com/ernesto/courses/hyperledger-fabric/hlf-chaincode-development) scenario, we will also test chaincode using docker-compose.