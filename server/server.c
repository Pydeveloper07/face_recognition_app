#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include <errno.h>
#include<arpa/inet.h>
#define PORTNO 9297

//gcc -shared -fPIC  -o libmy.so server.c

int sockfd, newsockfd;
pid_t childpid;
struct sockaddr_in serv_addr, cli_addr;
socklen_t clilen;

void ReceiveFile()
{
	FILE *fp;
	int bytesReceived = 0;
	char recvBuff[1024];
	char fname[100];
	read(newsockfd, fname, 256);
	//strcat(fname,"AK");
	printf("File Name: %s\n",fname);
	printf("Receiving file...");
   	fp = fopen(fname, "ab");
    	if(NULL == fp)
    	{
       	 printf("Error opening file");
    	}

	long double sz=1;
    /* Receive data in chunks of 256 bytes */
    	while((bytesReceived = read(newsockfd, recvBuff, 1024)) > 0)
   	 {
   	     sz++;
             fwrite(recvBuff, 1,bytesReceived,fp);
         }

        if(bytesReceived < 0)
         {
         	printf("\n Read Error \n");
         }
        printf("\nCompleted.\n");
}

char* ReadDatShit()
{
	int size = 100;
	char* buffer = malloc(size);
	int nn;
	bzero(buffer, size);	
	nn = read(newsockfd, buffer, size);
	if(nn<0)
		perror("Error on reading.");
		
	return buffer;

}


void CloseShit()
{
	
	close(newsockfd);
	close(sockfd);
	

}


int Forker()
{
	return (childpid = fork());
}

void NewProcess()
{
	newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
	if(newsockfd <0 )
	      perror("Error on Accept");
	printf("Connection accepted from %s:%d\n", inet_ntoa(cli_addr.sin_addr),ntohs(cli_addr.sin_port));
}
void SendDatShit(char *buffer)
{
	int nn;
	//bzero(buffer, sizeof(buffer));
	
	nn = write(newsockfd, buffer, strlen(buffer));
	if(nn<0)
		perror("Error on Writing!");
		
		
}


int main()
{
	
	int  nn;

	
	
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if(sockfd<0)
	{
		perror("Error opening socket");
	
	}
	bzero((char *) &serv_addr, sizeof(serv_addr));
	
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr= INADDR_ANY;
	serv_addr.sin_port = htons(PORTNO);
	
	if(bind(sockfd,(struct sockaddr *)&serv_addr, sizeof(serv_addr))<0)
		perror("Binding Failed.");
	printf("Bind to port %d\n", PORTNO);
	listen(sockfd, 5);
	clilen = sizeof(cli_addr);
	
	
	
	
	return 0;
}












