/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} target
 * @param {number} k
 * @return {number[]}
 */
import {deserialize} from './tree_node.js'

var distanceK = function(root, target, k) {
    const path={}//maps node to dist to target
    const ans=new Set()
    function build_path(node){
        if (node==null)
            return -1
        if (node==target){
            console.log('at target')
            path[node.val]={node,dist:0}
            return 0
        }
        for (const child of [node.left,node.right]){
            let dist=build_path(child)
            if (dist==-1)
                return -1
            dist+=1
            console.log(dist)
            path[child.val]={node:child,dist}
            return dist
        }
    }
    build_path(root)
    console.log(path)
    function f(node,k){
        if (k==0){
            ans.add(node.val)
            return
        }
        for (const child of [node.left,node.right].filter(Boolean)){        
            if (path[child.val]==null)
                f(child,k-1)
        }
    }
    for (const {node,k} of Object.values(path)){
        f(node,k)
    }
    return [...ans]
};
const tree=deserialize('[3,5,1,6,2,0,8,null,null,7,4]')
console.log(tree)