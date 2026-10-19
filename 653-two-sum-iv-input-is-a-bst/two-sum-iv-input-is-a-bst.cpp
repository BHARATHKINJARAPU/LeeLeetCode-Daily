class Solution {
    class BSTIterator {
        stack<TreeNode*> st;
        bool dir;
    public:
        BSTIterator(TreeNode* root, bool forward) : dir(forward) {
            pushAll(root);
        }
        bool hasNext() const { return !st.empty(); }
        int next() {
            TreeNode* node = st.top(); st.pop();
            pushAll(dir ? node->right : node->left);
            return node->val;
        }
    private:
        void pushAll(TreeNode* node) {
            while (node) {
                st.push(node);
                node = dir ? node->left : node->right;
            }
        }
    };

public:
    bool findTarget(TreeNode* root, int k) {
        if (!root) return false;
        BSTIterator lo(root, true);
        BSTIterator hi(root, false);
        int l = lo.next(), r = hi.next();
        while (l < r) {
            long long sum = (long long)l + r;
            if (sum == k) return true;
            if (sum < k) {
                if (!lo.hasNext()) break;
                l = lo.next();
            } else {
                if (!hi.hasNext()) break;
                r = hi.next();
            }
        }
        return false;
    }
};