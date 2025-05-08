class TreeNode {
  constructor(val) {
      this.val = val;
      this.left = null;
      this.right = null;
  }
}

export function deserialize(data) {
  if (!data) return null;

  const values = data.split(',');
  let index = 0;

  function buildTree() {
      const val = values[index++];
      if (val === 'null') return null;

      const node = new TreeNode(parseInt(val));
      node.left = buildTree();
      node.right = buildTree();
      return node;
  }

  return buildTree();
}