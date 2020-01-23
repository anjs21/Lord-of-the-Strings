import json
import os
import math
default_theives=3
usernames={}
score={} #
cop_scores={}
theif_scores={}
#return_code is 1 when cop wins, -1 is when theif wins
def update_total_scores():
	global score
	global cop_scores
	global theif_scores
	for key,values in usernames.items():
		score[key]=(0.0,0.0)
	for key,values in cop_scores.items():
		
		score[key[0]]=(score[key[0]][0]+values[0],score[key[0]][1]+values[1])
		
	for key,values in theif_scores.items():
		score[key[0]]=(score[key[0]][0]+values[0], score[key[0]][1]+values[1])
		
	
def eval_cop_score_innerfunc(return_code,theives_caught,blocks,total_theives):
	score1=0.0
	score2=0.0
	if return_code==1 and return_code<-1:
		score1=1
		score2=-blocks
	elif return_code==-1 and return_code>1:
		score1=0
		score2=(theives_caught*1.0)/(total_theives*1.0+1.0)
	else:
		pass
	return (score1,score2)

def eval_theif_score_innerfunc(return_code,theives_caught,blocks,total_theives):
	score1=0.0
	score2=0.0
	if(return_code>0):
		score1=0
		score2=0.2*blocks
	else:
		score1=1
		score2=-10.0*(theives_caught*1.0)/(total_theives*1.0+1.0)
	return (score1,score2) 

def eval_score(path_var):
	global default_theives
	zod_move =len( json.load( open(   os.path.join(path_var,"Zod's move.txt")    )  ) )
	jor_move =len( json.load(open(os.path.join(path_var,"Jor-El move.txt"))) )	
	theives_caught = len( json.load(open(os.path.join(path_var,"trap.txt"))) )	
	return_code =json.load(open(os.path.join(path_var,"returncode.txt")))[0]
	blocks= min( zod_move,jor_move)//2;
	scorecop=eval_cop_score_innerfunc(return_code,theives_caught,blocks,default_theives) 
	scoretheif=eval_theif_score_innerfunc(return_code,theives_caught,blocks,default_theives)
	return (scorecop,scoretheif)

def eval_game(username1,username2,path1,path2):#path1 for username1 being cop, path2 for the other game
	global usernames
	global cop_scores
	global theif_scores
	usernames[username1]=username1
	usernames[username2]=username2
	(scorecop1,scoretheif2)=eval_score(path1)
	(scorecop2,scoretheif1)=eval_score(path2)
	cop_scores[(username1,username2)]=scorecop1
	cop_scores[(username2,username1)]=scorecop2
	theif_scores[(username1,username2)]=scoretheif1
	theif_scores[(username2,username1)]=scoretheif2
	cop_scores[(username1,username1)]=(0,0)
	cop_scores[(username2,username2)]=(0,0)
	theif_scores[(username1,username1)]=(0,0)
	theif_scores[(username2,username2)]=(0,0)
	update_total_scores()

def main(path,user1,user2):
	global score
	u1 = user1
	u2 = user2
	p1 = os.path.join(path)
	p2 = os.path.join(path)
	eval_game(u1,u2,p1,p2)
	print(score)
 
main("./Sample/Sample","Sample1","Sample2")
