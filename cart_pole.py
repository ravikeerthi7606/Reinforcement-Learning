import gymnasium as gym
import matplotlib.pyplot as plt

env = gym.make("MountainCar-v0", render_mode="rgb_array")  # Create the CartPole environment with RGB rendering
state, info = env.reset(seed=42)  

def render():
    state_image = env.render()  
    plt.imshow(state_image)  
    plt.show()


for _ in range(5):
    action = env.action_space.sample()  # Take a random action
    state, reward, terminated, truncated, info = env.step(action)  # Step the environment
    if terminated or truncated:
        render()  
        state, info = env.reset()  # Reset the environment if done
          
env.close() 
   