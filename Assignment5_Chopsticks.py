/* Make player1 and player2 global variables */

def main():
	//call the start of the game and stuff
  bool player1_turn = False 
  player1 = Player()
  player2 = Player()
  //instructions printed
  while True:
  	/* plays game */
    //turn is swapped
    //display game environment -(print_hands())
    	//say whose turn it is
      //show the finger count for each 
      //each hand is labeled left or right
    //waits for user input
    	//loop until correct input
    //checks the input (breaking, if the input is quit) and calls either touch_opposing or touch_self
    	
    ///////(examples)
    player input:
    	left to right
    player input:
    	split 
      >>left: // will implicitly know how many fingers will be on the right hand 
      	//we are saying how many fingers we want on the left hand
    
    player1's turn
    they choose to use their left hand (3 fingers) to touch the oppsing players right hand (2 fingers)
    touch_opposing(player1.left_hand, player2.right_hand) //where left_hand and right_hand are ints
    
    printhands()
    Player 2		( R )			( L )
    						   |\			   \
     		 				  2			 		1
                  
    						||||
    Player 1		( L )			(R)
     		 				 4			 0
     
     Player 2's turn.
     >>left to left
     >>best_move //prints out current player's best move

def touch_opposing(hand_self, hand_opposing):
	/* hand_self is the hand the current player is using */
  /* hand_opposing is the hand of the opposing player that self is touching */
  /* checks if move is illegal e.i if either hand is 0 */
  //updates the oppsing players hand -- calling Player.add(hand_opposing, hand_self)
  //calls game_over_check()
  
def touch_self(hand_from, hand_to):
	/* move digits from hand_from to hand_to (subtraction/addition) */
  //updates current players hands

def check_score(Player1 object, Player2 object)
	//add total of player1.left_hand + player1.right_hand and player2.left_hand + player2.right_hand
  //

def game_over_check():
	//check hands of both players to determine if the game is over
  //if a player has two empty hands then the other player is the winner 
  	//prints a winner message (who won), then checks if replay (if so prints the instructions and resets the game)

def print_hands()
	//show hands as digits for both hands, repeat for both players
  //           P1             P2



///////////////////////////////////

class Player():
	def __init__():
  	self.left_hand = 1
	  self.right_hand = 1
    
  add(hand_opposing, hand_self, self):
  	//hand_opposing is the number of fingers of the opposing players hand
    //hand_self is the hand the opposing player touched (left or right)
    
    if hand_self == "L":
  		self.lefthand += hand_opposing
      if self.lefthand > 4:
      	self.lefthand = 0
        
    if hand_self == "R":
    	self.righthand += hand_opposing
      if self.righthand > 4:
      	self.righthand = 0
    