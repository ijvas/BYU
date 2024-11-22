def water_colum_height(tower_height, tank_height):
    water_column = tower_height + ( (3 * tank_height) / 4)
    return water_column



def pressure_gain_from_water_height(water_column_height):
    pressure = (998.2 * 9.80665 * water_column_height) / 1000
    return pressure



def pressure_loss_from_pipe(pipe_diameter, pipe_lenght, friction_factor, fluid_velocity):
    lost_pressure = (-friction_factor * pipe_lenght * 998.2 * (fluid_velocity**2)) / (2000 * pipe_diameter)
    return lost_pressure
