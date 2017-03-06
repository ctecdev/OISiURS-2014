class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def preorderTraversal(subtree):
    if subtree is not None:
        print(subtree.data)
        for node in subtree.children:
            preorderTraversal(node)

class TreeParentNode:
    def __init__(self):
        self.children=[]

def main():
    mRoot = TreeNode('---')
    mFile = TreeNode('File')
    mEdit = TreeNode('Edit')
    mTools = TreeNode('Tools')
    mRoot.children.append(mFile )
    mRoot.children.append(mEdit)
    mRoot.children.append(mTools)
                          
    mNew = TreeNode('New')
    mOpen = TreeNode('Open')
    mSave = TreeNode('Save')
    mSaveAs = TreeNode('Save As')
    mQuit = TreeNode('Quit')
    mFile.children.append(mNew)
    mFile.children.append(mOpen)
    mFile.children.append(mSave)
    mFile.children.append(mSaveAs)
    mFile.children.append(mQuit)

    mCut = TreeNode('Cut')
    mCopy = TreeNode('Copy')
    mPaste = TreeNode('Paste')
    mSelectAll = TreeNode('Select All')
    mEdit.children.append(mCut)
    mEdit.children.append(mCopy)
    mEdit.children.append(mPaste)
    mEdit.children.append(mSelectAll)
                          
    mSort1 = TreeNode('Sort ascending')
    mSort2 = TreeNode('Sort descending')
    mTools.children.append(mSort1)
    mTools.children.append(mSort2)
    
    preorderTraversal(mRoot)
    
if __name__=="__main__":
    main()
    