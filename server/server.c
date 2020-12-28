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
	int received_int = 0;
	read(newsockfd, fname, 256);
	read(newsockfd, &received_int, sizeof(received_int));
	//strcat(fname,"AK");
	printf("File Name: %s\n",fname);
	printf("Receiving file...");
   	fp = fopen(fname, "ab");
    	if(NULL == fp)
    	{
       	 printf("Error opening file");
    	}

	long double sz=1;
    /* Receive data in chunks of 1024 bytes */

    int allbytes = 0;
    int k = 0;

    	while(1)
    	{
    	    bytesReceived = read(newsockfd, recvBuff, 1024);
   	        allbytes+=bytesReceived;
   	        if (allbytes==ntohl(received_int))
   	        {
   	     	    break;
   	        }

   	        sz++;

            fwrite(recvBuff, 1,bytesReceived,fp);
         }

        if(bytesReceived < 0)
         {
         	printf("\n Read Error \n");
         }
        printf("\nCompleted.\n");
        fclose(fp);
}

char* ReadDatShit()
{
	int buflen = 0;
	int nn;

    // get size of data
	nn = read(newsockfd, (char *)&buflen, sizeof(buflen));
    if(nn<0)
		perror("Error on 1st reading.");


    // allocate memory of size 'buflen'
    buflen = ntohl(buflen);
    char *buffer = malloc(buflen);
    bzero(buffer, buflen);

    //reading data from socket
    FILE *fp = fdopen(dup(newsockfd), "r");
    nn = fread(buffer, 1, buflen, fp);
    fclose(fp);

    //remove unnecessary part
    buffer[buflen] = '\0';
    if(nn<0)
		perror("Error on 2nd reading.");

	return buffer;

}

void Closesockfd()
{
    close(sockfd);
}

void Closenewsockdf()
{
    close(newsockfd);
}



int Forker()
{
	return (childpid = fork());
}

void NewProcess()
{
	newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
	if(newsockfd <0 )
	      exit(1);
	printf("Connection accepted from %s:%d\n", inet_ntoa(cli_addr.sin_addr),ntohs(cli_addr.sin_port));
}

void SendDatShit(char *buffer)
{

    int nn;
    // size of buffer in network byte order
    int bnum = htonl(strlen(buffer));

    // sending size of buffer
    nn = write(newsockfd, (char *)&bnum, sizeof(bnum));
	if(nn<0)
		perror("Error on 1st Writing!");

    // opening file stream. file descriptor is duplicated to safely close filestream
	FILE *fp = fdopen(dup(newsockfd), "w");

    // sending data and closing file stream
	nn = fwrite(buffer, 1, strlen(buffer), fp);
	fclose(fp);
    if(nn<0)
		perror("Error on 2nd Writing!");

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