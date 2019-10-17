
**Step 12:** Let us now run the program. You should see the output with count for each movie in a List collection as shown in the screenshot below.

 To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.countByMovieMain"`{{execute}} 

Please note caution while using accumulators. If the output generated from the accumulator is huge data, you should not use the accumulators. Instead, you should use the transformations as required. In this we case, the result of accumulator is just movies and their counts. It is not a huge data. We have achieved our result without shuffling the data across the network, which is usually the case with transformations.

Task is complete!

