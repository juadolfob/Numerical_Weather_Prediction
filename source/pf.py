

class f:

    @staticmethod
    def p(m, v):
        return m * v

    @staticmethod
    def velocity_average(distance, delta_time):
        return distance / delta_time

    @staticmethod
    def velocity(delta_x, delta_time):
        return delta_x / delta_time

    @staticmethod
    def delta_position(position, velocity, delta_time):
        return position+velocity*delta_time

    @staticmethod
    def aceleration(position, delta_velocity, delta_time):
        return delta_velocity * delta_time
