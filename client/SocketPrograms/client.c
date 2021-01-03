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

int fsize(char* file) {
  int size;
  FILE* fh;

  fh = fopen(file, "rb"); //binary mode
  if(fh != NULL){
    if( fseek(fh, 0, SEEK_END) ){
      fclose(fh);
      return -1;
    }

    size = ftell(fh);
    fclose(fh);
    return size;
  }

  return -1; //error
}



void SendData(char *buffer)
{
	int nn;
    int bnum = htonl(strlen(buffer));
	//bzero(buffer, sizeof(buffer));

    nn = write(sockfd, (char *)&bnum, sizeof(bnum));
	if(nn<0)
		perror("Error on 1st Writing!");

    //printf("%s", buffer);
    nn = write(sockfd, buffer, strlen(buffer));

	if(nn<0)
		perror("Error on 2nd Writing!");

}

char* ReadData()
{
    int buflen = 0;
	int nn;

    // get size of data
	nn = read(sockfd, (char *)&buflen, sizeof(buflen));
    if(nn<0)
		perror("Error on 1st reading.");

    // allocate memory of size 'buflen'
    buflen = ntohl(buflen);
    char *buffer = malloc(buflen);
    bzero(buffer, buflen);

    //read data from socket
    FILE *fp = fdopen(dup(sockfd), "r");
    nn = fread(buffer, 1, buflen, fp);
    fclose(fp);

    //remove unnecessary part
    buffer[buflen] = '\0';
    if(nn<0)
		perror("Error on 2nd reading.");

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