# WEEK 7

## MULTI-ARMED BANDITS- MOVIE RECOMMENDATION 

1. Write down the “Movie Recommendation” as a Reinforcement Learning problem formulation. Use comment lines for proper documentation.

2. For the environment, use the built-in TF-agent agent, MovieLensPyEnvironment (non-per-arm) 
https://github.com/tensorflow/agents/blob/master/tf_agents/bandits/environments/movielens_py_environment.py 

3. Compute the regret using the built-in metric in TF-agents 
https://github.com/tensorflow/agents/blob/master/tf_agents/bandits/metrics/tf_metrics.py 

4. Plot the regret against 20,000-time steps using the built-in agents:
`a. LinUCB`, `b. LinTS`, `c. EpsilonGreedy`
And identify the best agent for the movie recommendation 

5. Write the Recommendation policy, given a new observation request (i.e. a user vector), the 
policy will produce actions, which are the recommended movies 
