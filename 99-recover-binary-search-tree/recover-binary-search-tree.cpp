class Solution {
public:
    void recoverTree(TreeNode* root) {
        TreeNode* first = nullptr;
        TreeNode* second = nullptr;
        TreeNode* prev = nullptr;
        TreeNode* cur = root;

        while (cur) {
            if (!cur->left) {
                // Visit cur
                if (prev && prev->val > cur->val) {
                    if (!first) first = prev;
                    second = cur;
                }
                prev = cur;
                cur = cur->right;
            } else {
                // Find inorder predecessor
                TreeNode* pred = cur->left;
                while (pred->right && pred->right != cur)
                    pred = pred->right;

                if (!pred->right) {
                    pred->right = cur;  // Thread
                    cur = cur->left;
                } else {
                    pred->right = nullptr;  // Remove thread
                    // Visit cur
                    if (prev && prev->val > cur->val) {
                        if (!first) first = prev;
                        second = cur;
                    }
                    prev = cur;
                    cur = cur->right;
                }
            }
        }

        if (first && second)
            std::swap(first->val, second->val);
    }
};