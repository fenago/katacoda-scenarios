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

Assuming there are no errors, now we can proceed to the next step, testing your chaincode.