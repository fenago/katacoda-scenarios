#### Run AvroProducer
Run the main method of the `AvroProducer` in **terminal 2** by running following command.
`cd ~/kafka/Chapter05/kioto && java -cp ./build/libs/kioto-0.1.0.jar kioto.avro.AvroProducer`{{execute T2}} 


The output on the console consumer **(terminal 1)** should be similar to the one shown here:

```
HEALTH_CHECKLake JeromyGE50-GF78HYDROELECTRICRUNNING�����Y,B227.30.250.185
HEALTH_CHECKLockmanlandMW69-LS32GEOTHERMALRUNNING֗���YB72.194.121.48
HEALTH_CHECKEast IsidrofortIH27-WB64NUCLEARSHUTTING_DOWN�̤��YB88.136.134.241
HEALTH_CHECKSipesshireDH05-YR95HYDROELECTRICRUNNING����Y�B254.125.63.235
HEALTH_CHECKPort EmeliaportDJ83-UO93GEOTHERMALRUNNING���Y�A190.160.48.125
```

**Important:** 
- Interface will keep switching back to terminal 1 because consumer is running there after executing command, you can manually switch by clicking `terminal 2`.
- Press `Ctrl` + `C` in terminal 1 and 2 to stop everything before proceeding to next step.
