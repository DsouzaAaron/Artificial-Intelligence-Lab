# WEEK 5

## MULTI ARMED BANDITS IN TF-AGENTS 

1. Do the tutorial for MAB in TF-Agents 
https://www.tensorflow.org/agents/tutorials/bandits_tutorial 

2. Exercise 1 - <br>
a.  Create a environment a. for which the observation is a random integer between 
-5 and 5, there are 3 possible actions (0, 1, 2), and the reward is the product of the action and 
the observation. <br>
b. Define an optimal policy manually. The action only depends on the sign of the observation, 0 
when is negative and 2 when is positive. <br>
c. Request for 50 observations from the environment, compute and print the total reward. 
3. Exercise 2 – <br>
a.  Create an environment a. Define an environment will either always give reward = 
observation * action or reward = -observation * action. This will be decided when the 
environment is initialized. <br>
b. Define a policy that detects the behavior of the underlying environment. There are three 
situations that the policy needs to handle: 
<br>
一 i. The agent has not detected know yet which version of the environment is running. <br>
一 ii. The agent detected that the original version of the environment is running. <br>
一 iii. The agent detected that the flipped version of the environment is running. <br>
c. Define the agent that detects the sign of the environment and sets the policy 
appropriately.