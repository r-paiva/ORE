import ore, crypto, random, os

print("Prototype of Order-Revealing Encryption")

random.seed(os.urandom(128))
tests_ok = 0
tests_failed = 0
tests = 10000

for i in range(0, tests):
    # Generate random key from system random pool
    key = crypto.generate_prf_key(64)

    # Generate random value (1000 <= r < 5000)
    # Currently does not support negative number comparison (due to the extra bit manipulation required
    # which is not implemented)
    r1 = random.randint(1000, 5000)
    r2 = random.randint(1000, 5000)
    print("#######################")
    print("r1 ->", r1)
    print("r2 ->", r2)
    # Encrypt first number
    ctx1 = ore.encrypt(key, r1)
    print("ctx1 -> ", ctx1)
    # Encrypt second number
    ctx2 = ore.encrypt(key, r2)
    print("ctx2 -> ", ctx2)
    # Compare Ciphertexts
    result = ore.compare(ctx1, ctx2)

    # Print results
    if r1 < r2 and result == -1:
        print(result, " - [OK]")
        tests_ok += 1
    elif r1 > r2 and result == 1:
         print(result, " - [OK]")
         tests_ok += 1
    elif r1 == r2 and result == 0:
        print(result, " - [OK]")
        tests_ok += 1
    else:
        print(result, " - FAILED")
        tests_failed += 1
    print("#######################")

print("Number of Tests -> ", tests)
print("TESTES PASSED -> ", tests_ok)
print("TESTES FAILED -> ", tests_failed)
