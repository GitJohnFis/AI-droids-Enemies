# AI-dr0id Enemies
 _"*AI ENEMIES INBOUND*"_

<!--![AsteroidAIdroid](https://github.com/user-attachments/assets/1b975e9b-ce23-46bb-b180-f59912da219a)

![asteroids_start_animation](https://github.com/user-attachments/assets/5bc89868-cc50-454e-9673-5bff3fd40b9d)-->


![asteroids_zoom_blur_animation (1)](https://github.com/user-attachments/assets/6eb4e346-e7bc-4fee-8675-8439351116c4)
> *Basic AI movement*

> *Enemy Droid Ship Atk logic*

> *State based AI dr0ids*
- AGRO
- DEFENSE
- RETREAT
> *Boss Fights*

> *Formation flying (dynamic)*
---
## Installing Julia Dependencies

Run the following commands in your terminal to install Julia and its dependencies:

```bash
# Update package lists
sudo apt update

# Install dependencies (optional but recommended)
sudo apt install -y wget

# Download Julia (replace version with latest stable)
wget https://julialang-s3.julialang.org/bin/linux/x64/1.9/julia-1.9.3-linux-x86_64.tar.gz

# Extract it to /opt (or wherever you want)
sudo tar -xvzf julia-1.9.3-linux-x86_64.tar.gz -C /opt/

# Create a symlink for easy access
sudo ln -s /opt/julia-1.9.3/bin/julia /usr/local/bin/julia

# Verify installation
julia --version
