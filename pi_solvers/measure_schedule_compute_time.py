from pi_solvers.solver_lib import get_pi_schedule
import time

if __name__ == "__main__":
    time = time.time()
    get_pi_schedule(50, 0, "../data/ffhq/pi_adaptive/_t.csv")
    print(time.time() - time)