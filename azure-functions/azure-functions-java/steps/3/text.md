In an empty folder, run the following command to generate the Functions project from a Maven archetype.

```mvn archetype:generate \
    -DarchetypeGroupId=com.microsoft.azure \
	-DarchetypeArtifactId=azure-functions-archetype```{{execute T1}}


Maven will ask you for values needed to finish generating the project. For `groupId`, `artifactId`, and `version` values. The appName value must be unique across Azure, so Maven generates an app name based on the previously entered artifactId as a default. The packageName value determines the Java package for the generated function code.

**Note:** We will provide values and finish generating the project in the next step.