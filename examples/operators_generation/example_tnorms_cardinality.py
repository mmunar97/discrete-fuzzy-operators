import time
import pickle

from discrete_fuzzy_operators.generators.tnorms.fuzzy_tnorms_recursive_counter import count_tnorms


if __name__ == "__main__":

    t = time.time()

    generation_limit = 20
    count = count_tnorms(depth_max=generation_limit)

    print(f"NUMBER OF T-NORMS UP TO n={generation_limit}")
    print(count)
    print("ELAPSED TIME")
    print(time.time()-t)

    with open("results.txt", "wb") as file:
        pickle.dump(count, file)

