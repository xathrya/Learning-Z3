#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
  crackme.c
  Created by Roland Sako on 18/02/16.
*/

int sameAtIndex(int g1[], int g2[]){
	int i;
	for(i=0; i < 4; i++){
		if (g1[i] == g2[i]){
			return 1;
		}
	}
	return 0;
}

int toi(char c){
	return c-48;
}

int check_serial(char *s){

	//check the length
	if (strlen(s) != 19){
		return 0;
	}
	
	//check format is xxxx-xxxx-xxxx-xxxx
	int i;
	for(i=4; i<20; i=i+5){
		if (i<15 && s[i] != '-'){
			return 0;
		}
		
		//check if it's numbers
		int j;
		for (j=i-4; j<i; j++){
			if (s[j] < 48 || s[j] > 57){
				return 0;
			}
		}
	}


	
	int first[4] = {toi(s[0]), toi(s[1]), toi(s[2]), toi(s[3])};
	int second[4] = {toi(s[5]), toi(s[6]), toi(s[7]), toi(s[8])};
	int third[4] = {toi(s[10]), toi(s[11]), toi(s[12]), toi(s[13])};
	int fourth[4] = {toi(s[15]), toi(s[16]), toi(s[17]), toi(s[18])};

	int sum_first = first[0]+first[1]+first[2]+first[3];
	int sum_second = second[0]+second[1]+second[2]+second[3];
	int sum_third = third[0]+third[1]+third[2]+third[3];
	int sum_fourth = fourth[0]+fourth[1]+fourth[2]+fourth[3];

	int avg_sums = (sum_first+sum_second+sum_third)/3;

	//constraint 2
	for(i=0; i<4; i++){
		if (fourth[i] < 3 || fourth[i] > 8){
			return 0;
		}
	}
	
	//constraint 3.1
	if(sum_fourth != avg_sums){
		return 0;
	}

	//constraint 3.2
	if(sum_first != sum_fourth/4){
		return 0;
	}
	
	//constraint 4
	if(sum_first == sum_second){
		return 0;
	}

	//constraints 5 and 6
	if(sameAtIndex(first, fourth) || sameAtIndex(second, third)){
		return 0;
	}

	return 1;

}


int main(int argc, char *argv[]){
	if (argc < 2){
		printf("usage: %s <serial number>\n", argv[0]);
		return 0;
	}
	char *serial = argv[1];
	if (check_serial(serial) == 1){
		printf("\n##############      Good  Job!      ##############\n############## The serial is valid! ##############\n\n");
	
	}else{
		printf("\n##############   Try  again!   ##############\n############## Invalid serial! ##############\n\n");
	}
}





