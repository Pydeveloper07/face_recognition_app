//change functions according to your need but don't worked to update shared library
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>

#define PORTNO 9297

int sockfd;


void SendDatShit(char *buffer)
{
	int nn;
	
	//bzero(buffer, sizeof(buffer));
	nn = write(sockfd, buffer, strlen(buffer));
	if(nn<0)
		perror("Error on Writing!");
		
		
}

char* ReadDatShit()
{
	int size = 100;
	char* buffer = malloc(size);
	int nn;
	bzero(buffer, size);	
	nn = read(sockfd, buffer, size);
	
	//printf("ResClient : %s\n", buffer);
	if(nn<0)
		perror("Error on reading.");
		
	return buffer;

}

void CloseShit()
{

	close(sockfd);

}


int main(int argc, char *argv[])
{
	int n;
	
	struct sockaddr_in serv_addr;
	
	char buffer[255];
	
	sockfd = socket(AF_INET, SOCK_STREAM,0);
	if(sockfd < 0)
		perror("ERROR opening socket");
	

	
	bzero((char *) &serv_addr, sizeof(serv_addr));
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(PORTNO);
	serv_addr.sin_addr.s_addr=inet_addr("127.0.0.1");
	if(connect(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr))<0)
		perror("Connection Failed");
        
	
	
	
	return 0;
}
