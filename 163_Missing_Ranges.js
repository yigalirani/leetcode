var findMissingRanges = function(nums, lower, upper) {

    const ans=[]
    for (const x of nums){
        if (x>lower){
            ans.push([lower,x-1])
        }
        lower=x+1

    }

    if (upper>=lower)
        ans.push([lower,upper])
    return ans
};