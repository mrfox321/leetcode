def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        if amount == 0:
            return 0
        if amount < coins[0]:
            return -1

        #remove large coins
        for index,coin in enumerate(coins):
            if coin > amount:
                coins = coins[:index]
        val = [0]
        for i in xrange(1,amount+1):
            space = [1+val[i-coin] for coin in coins if coin <= i]
            if not space:
                val.append(amount+1)
            else:
                val.append(min(space))

        if val[-1] > amount:
            return -1
        else:
            return val[-1]
    
