class StoryNode:
    """Represents a node in the decision tree."""
    def __init__(self, event_number, description, left=None, right=None):
        self.event_number = event_number
        self.description = description
        self.left = left
        self.right = right

class GameDecisionTree:
    """Binary decision tree for the RPG."""
    def __init__(self):
        self.nodes = {}
        self.root = None

    def insert(self, event_number, description, left_event=None, right_event=None):
        """Insert a new story node into the tree."""
        if event_number not in self.nodes:
            self.nodes[event_number] = StoryNode(event_number, description)
        node = self.nodes[event_number]
        node.description = description
        if left_event is not None:
            if left_event not in self.nodes:
                self.nodes[left_event] = StoryNode(left_event, "")
            node.left = self.nodes[left_event]
        if right_event is not None:
            if right_event not in self.nodes:
                self.nodes[right_event] = StoryNode(right_event, "")
            node.right = self.nodes[right_event]
        if self.root is None:
            self.root = node

    def play_game(self):
        """Interactive function that plays the RPG."""
        current_node = self.root
        while current_node:
            print(current_node.description)
            if current_node.left is None and current_node.right is None:
                print("The end.")
                break
            choice = input("Enter '1' for left or '2' for right: ").strip()
            if choice == '1' and current_node.left:
                current_node = current_node.left
            elif choice == '2' and current_node.right:
                current_node = current_node.right
            else:
                print("Invalid choice. Try again.")

def load_story(filename, game_tree):
    """Load story from a file and construct the decision tree."""
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split('|')
            event_number = int(parts[0].strip())
            description = parts[1].strip()
            left_event = int(parts[2].strip()) if parts[2].strip() != '-1' else None
            right_event = int(parts[3].strip()) if parts[3].strip() != '-1' else None
            game_tree.insert(event_number, description, left_event, right_event)

# Main program
if __name__ == "__main__":
    print("TODO: Initialize the GameDecisionTree and load story data")
    game_tree = GameDecisionTree()

    print("TODO: Load the story from 'story.txt'")
    load_story("story.txt", game_tree)

    print("TODO: Start the RPG game")
    game_tree.play_game()
