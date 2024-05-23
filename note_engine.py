from llama_index.tools import FunctionTool
import os

note_file = os.path.join("data", "notes.txt")

def save_note(note):
    """
    Appends a note to a file, creating the file if it does not exist.

    This function checks if a specific file (defined by the variable `note_file`) exists. 
    If the file does not exist, it creates an empty file. Then, it opens the file in 
    append mode and writes the provided note to it, followed by a newline character.

    Args:
        note (str): The note to be saved to the file.

    Returns:
        str: A confirmation message indicating that the note was saved.
    """

    if not os.path.exists(note_file):
        open(note_file, "w")
    
    with open(note_file, "a") as f:
        f.writelines([note + "\n"])

    return "note saved"

note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="this tool can save a text based note to a file for the user"
)