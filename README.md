# Launchdarkly Solutions Engineer Assessment

This is the final version of my assessment submission. It's an application built with Python and the Flask framework. The Feature Flag displays a third button option to a user when the flag is toggled "On" and the user uses an email with the word "manager" in it.

The reason for this is to allow specific features to be available for managers in a company and not for their employees. In an authentic scenario, there would be more complexities, but for this demo, I feel it's enough.

## Env Prerequisite 

-> Python3 and PIP3 setup is installed and configured.

-> An active [LaunchDarkly account](https://app.launchdarkly.com/login) with the ability to create a flag.

-> Basic knowledge of the Python and JavaScript programming languages.

## Setup the Launchdarkly Environment and Project
We will set up a Launchdarkly project and environment where the feature flags will be created. 
To create a new project;

 1. Navigate to the [accounts setting](https://app.launchdarkly.com/settings/projects) page.
 2. Click the **Projects** tab.
 3. Select **Create Project**.
 4. The Create a project panel will appear.
 5. Give the project a human-readable name.
 6. Select **Create Project**. 
 7. You will be returned to the Projects tab.
 8. Click the new project's SDK key to copy.

![SDK Locations](https://github.com/dajabu/LDAssessment/blob/main/assets/Screenshot%202022-06-02%20at%2023.51.02.png)

## Installing the Python SDK
In the `requirements` file, make sure
`launchdarkly-server-sdk`
is present.
![Requirements File](https://github.com/dajabu/LDAssessment/blob/main/assets/Screenshot%202022-06-03%20at%2012.19.21.png)

The requirements file details all of the necessary modules the Python app depends on.

##  Initializing the LaunchDarkly client

After installing the SDK, you can import and initialize the client into the code.

 1. Make sure the following code is in the server.py file; 
 `import ldclient`

## Creating the Flag

 1. In Launchdarkly, navigate to the Feature Flag dashboard.
 2. Click **Create Flag**.
 3. Enter "Manager Button" as the name and (optionally) add a description.
 4. Leave the flag variation set to **Boolean**.
 5. Tick "SDKs using Client-Side ID.
 6. Set the default rule to **False**.
![Flag Creation 1](https://github.com/dajabu/LDAssessment/blob/main/assets/Screenshot%202022-06-03%20at%2000.28.07.png)
![Flag Creation 2](https://github.com/dajabu/LDAssessment/blob/main/assets/Screenshot%202022-06-03%20at%2000.28.33.png)
 7. Click "Save Flag"
 8. Select your Feature Flag and select the targeting tab.
 9. In "Select an Attribute", select **email**.
 10. Set the operator to **contains**. 
 11. Enter the word "**manager**"
 12. Review and Save.
 ![Flag Targeting](https://github.com/dajabu/LDAssessment/blob/main/assets/Screenshot%202022-06-03%20at%2012.29.33.png)
 For any user with "manager", the Leave Request App will be visible.

## Setup The Application

 1. Clone this repository. [Git Repo](https://github.com/dajabu/LDAssessment.git)
 2. In the .env file, assign the **SDK key** you copied earlier to the environment variable `LD_SDK_KEY`
![.env file](https://github.com/dajabu/LDAssessment/blob/main/assets/Screenshot%202022-06-03%20at%2012.33.18.png)
 
 3. Open a terminal in the repository root.
 4. Run the command `npm run start`
 
Once the dependencies are installed and the application has started, you will see something like the below log in your terminal;
  `Running on http://127.0.0.1:5000`
 
 5. Open your browser and enter the URL.
 6. You will see buttons available and a login button in the top right.
 7. Select the login and enter any email address.
 8. You will see that the two buttons are still there.
 9. Logout and log in again with a user email that contains the word "manager"
 10. You will see that a 3 button is available.
 11. The feature flag is working. The third button only appears when the feature flag is enabled and using targeting, only managers will see it.
![Application](https://github.com/dajabu/LDAssessment/blob/main/assets/Screenshot%202022-06-03%20at%2012.42.45.png)
