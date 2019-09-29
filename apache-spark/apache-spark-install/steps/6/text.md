

Step 4: Let us now set up the environment variables for Spark. Execute the following command to do so.

$ sudo vi ~/.bashrc

 

The file should open as shown below.
 
RDD op.

IntelliJ D/l & Ins
Configure IntelliJ


 

Now press i key to edit the file and append the following environment variable at the end of the file.

SPARK_HOME=/usr/share/spark
Export PATH=$SPARK_HOME/bin:$PATH









 
RDD op.

IntelliJ D/l & Ins
Configure IntelliJ

 

After you have finished appending the text above, hit the Esc on your keyboard to stop editing and then press Shift - Z - Z to exit out of the editor by saving the changes. (Please see that you need to press Z twice while holding Shift key.)

Now reload the modified .bashrc file using the following command.

$ source ~/.bashrc