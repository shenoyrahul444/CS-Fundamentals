def rec_coin(target,coins):
        min_coins = target
        if target in coins:
            return 1
        else:
            for value in [ c for c in coins if c<= target]:
                num_coins = rec_coin(target-value, coins) + 1
                min_coins = min(num_coins, min_coins)
        return min_coins

print(rec_coin(6,[1,2,5]))

