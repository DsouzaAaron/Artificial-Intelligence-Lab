# WEEK 8 

## MDP & DYNAMIC PROGRAMMING

Use the Frozen Lake environment.
https://www.gymlibrary.dev/environments/toy_text/frozen_lake/
Learn the optimal policy for the frozen lake environment using the Policy Iteration vs the 
Value Iteration technique.

1. Create a Policy Iteration function with the following parameters <br>
• policy: 2D array of a size n(S) x n(A), each cell represents a probability of taking 
action a in state s. <br>
• environment: Initialized OpenAI gym environment object <br>
• discount_factor: MDP discount factor <br>
• theta: A threshold of a value function change. Once the update to value function is below this number <br>
• max_iterations: Maximum number of iterations 

2. Create a Value Iteration function with the following parameters <br>
a. environment: Initialized OpenAI gym environment object <br>
b. discount_factor: MDP discount factor <br>
c. theta: A threshold of a value function change. Once the update to value function is below this number <br>
d. max_iterations: Maximum number of iterations

3. Compare the number of wins, average return after 1000 episodes and comment on which method performed better.