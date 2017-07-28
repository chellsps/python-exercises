You can't merge with local modifications. Git protects you from losing potentially important changes.
You have three options. 
1. Commit the change using
   git commit -m "My message"
2. Stash it.
Stashing acts as a stack, where you can push changes, and you pop them in reverse order.
To stash type:
git stash
Do the merge, and then pull the stash:
git stash pop
3. Discard the local changes
using git reset --hard


art [3:38 PM] 
git commit --amend -m “New commit message”



