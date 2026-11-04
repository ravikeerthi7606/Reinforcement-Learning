import gymnasium as gym
import matplotlib.pyplot as plt

env = gym.make("CartPole", render_mode="rgb_array")  # Create the CartPole environment with RGB rendering
state, info = env.reset(seed=42)  

def render():
    state_image = env.render()  
    plt.imshow(state_image)  
    plt.show()

render()

# for _ in range(1000):
#     action = env.action_space.sample()  # Take a random action
#     state, reward, terminated, truncated, info = env.step(action)  # Step the environment
#     if terminated or truncated:
#         state, info = env.reset()  # Reset the environment if done
    