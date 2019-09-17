In the search field, type `timer` and configure the new trigger with the settings as specified in the table below the image.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-timer/steps/4/timer.JPG)


Setting	| Suggested value | Description
--- | --- | ---
`Name` | *Default*	| Defines the name of your timer triggered function.
`Schedule` |	`0 */1 * * * *` | A six field CRON expression that schedules your function to run every minute.


Click **Create**. A function is created in your chosen language that runs every minute.

#### Verify
Verify execution by viewing trace information written to the logs.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-trigger-timer/steps/4/verify.JPG)
