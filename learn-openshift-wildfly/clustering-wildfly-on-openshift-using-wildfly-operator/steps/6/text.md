Now let's scale down the Pods, by editing the Operator configuration:
kubectl edit wildflyserver clusterbench

Set the size parameter to 1 and save the changes from the editor. Next, check that the Pods have scaled down:


