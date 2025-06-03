using PyCall
using Test

# Set the Python environment if needed
println(PyCall.python)

# Import pygame and your Python module (assumes enemy_ship.py is in the same folder)
pygame = pyimport("pygame")
pygame.init()  # Initialize pygame if needed

pushfirst!(PyVector(pyimport("sys")."path"), pwd())

#import the aiTracking module
air = pyimport("aiTracking")


# Test EnemyShip creation
@testset "EnemyShip basic functionality" begin
	enemy = air.EnemyShip(10, 10)
	@test enemy.x == 10
	@test enemy.y == 10
	@test enemy.state == "normal" #default state
	@test enemy.rect.width == 40
	@test enemy.rect.height == 40

	# Test movement toward a player
	player_x, player_y = 20, 20
	old_x, old_y = enemy.x, enemy.y
	enemy.move_towards_player(player_x, player_y)
	@test (enemy.x != old_x) || (enemy.y != old_y)
end

println("All tests completed.")


#Optional: quit pygame when done
pygame.quit()

println("All tests completed.")
# Uncomment the following lines if you want to run the tests using PyCall
# Uncomment the following lines if you want to run the tests


# using PyCall
# using Test

# # Import your Python module
# pyimport("pygame") #ensure game is eavailable in the python env
# enemy_mod = pyimport("enemy") #following the pa5th of the filepath enemy_ship.py
# state_machine = pyimport("state_machine")

# # Call a Python function/class...
# function test_enemy_ship()
#      # Create an EnemyShip at (0, 0)
#     enemy = enemy_mod.EnemyShip(0, 0)
#     # Target position for the player
#     player_x, player_y = 30, 40

#     # Save initial position
#     initial_x, initial_y = enemy.x, enemy.y

#     # Move enemy towards player
#     enemy.move_towards_player(player_x, player_y)

#     # After moving, enemy should not be at the same position
#     @test (enemy.x != initial_x) || (enemy.y != initial_y)

#     # Check the ship moved closer to the player
#     old_dist = sqrt((initial_x - player_x)^2 + (initial_y - player_y)^2)
#     new_dist = sqrt((enemy.x - player_x)^2 + (enemy.y - player_y)^2)
#     @test new_dist < old_dist

#     println("Enemy movement logic test passed!")
# end

# test_enemy_movement()

# # Define some tests for the state_machine
# function test_transition()
#     @assert state_machine.transition_state("idle", "start") == "running"
#     @assert state_machine.transition_state("running", "stop") == "idle"
#     @assert state_machine.transition_state("idle", "stop") == "idle"
#     println("All tests passed!")
# end

# test_transition()
# # result = state_machine.transition_state("idle", "start")