#include<string.h>
#include<stdio.h>
#include<stdlib.h>
typedef struct mobile{
                        char name[100];
                        char phone1[100];
                        char phone2[100];
                        char phone3[100];
                        char email[100];
                         }mob;
typedef struct name{
                   char name[100];
                         }name;
                         
                         
void strrev(char str[])
{

   int i,j;
   char temp;
   for(i=0;str[i]!=0;i++);
   for(j=0;j<(i/2);j++)
	{
      temp=str[j];
   	  str[j]=str[i-1-j];
      str[i-1-j]=temp;	 
 	}
	
 } 

int  genvcf(int n)
{
    
    FILE *csv, *vcf;
    csv=fopen("/home/taneesh/Development/Judaav/Judaavcsv.csv", "a");
    fprintf(csv, "\n" );
    fclose(csv);
    csv=fopen("/home/taneesh/Development/Judaav/Judaavcsv.csv", "r");
    vcf=fopen("Contacts.vcf", "w");
    char y;
    fscanf(csv, "%c", &y);
    while(y!='\n')
    {
        fscanf(csv, "%c", &y);
    }
    

    int i,j,k;
    char arr[100];
    char c,a;
    char prefix[100];
    char suffix[100];
    
    printf("a");
    
    
    for(i=0;i<100;i++)
     arr[i]=0;
    strcpy(prefix,arr);

    strcpy(suffix,arr);	

  char space[100];
  space[0]=' ';
  space[1]=0;
int q=0;

int flag=0;

char aux[100];

    printf("%d\n", n);
    mob person[n];
    for(i=0;i<n;i++)
    {
        printf("\n");
	      strcpy(aux,prefix);
        j=0;
        fscanf(csv,"%c",&c);
        k=0;

        while(c!='\n' || c!=EOF)
        {

            if(c==',')
            {
                arr[k]=0;
                
                if(j==0)
                {
                	strcat(arr,space);
                	strcat(aux,arr);
                	strcpy(person[i].name,aux);	  
                }
                
                else if(j==1)
                {
                    strcpy(person[i].phone1,arr);    
                }
            
               else if(j==2)
                {
                   strcpy(person[i].phone2,arr);    
                }
                
                else if(j==3)
                {
                    
                    strcpy(person[i].phone3,arr);
            		if(i==(n-1))
            		{
            		  for(q=0;q<k;q++)
                        arr[q]=0;
            		   scanf("%s",arr);
            		   
            		   strcpy(person[i].email,arr);
            		   flag=1;
            		    break;
					      }
            		  
					
                }

                j++;
                k=0;   
                
            }
            
            else
            {

                arr[k]=c;
                k++;
            }

            
            fscanf(csv,"%c",&c);    


        }
    // if(flag==1)
    //         break;

		arr[k]=0;
	    strcpy(person[i].email,arr);
	

    }
   fclose(csv);
name collect[3];
int z,l,o,m;
for(i=0;i<n;i++)
{ 
    
  for(z=0;z<3;z++)
   collect[z].name[0]=0;

  fprintf(vcf,"BEGIN:VCARD\n");
  fprintf(vcf,"VERSION:3.0\n");
  fprintf(vcf,"N:");
 l=0;
 j=0;
 o=0;
 m=0;
 strrev(person[i].name);
 while((person[i].name[j]!=0))
    { 
    if(l<=1)
   	 	{
   	 		if(person[i].name[j+1]==' ')
            {
            	
             collect[l].name[o]=person[i].name[j];
              collect[l].name[o+1]=0;
              strrev(collect[l].name);
              j+=2;
              l++;
              o=0;
             continue;
             }
        else
         {
           collect[l].name[o]=person[i].name[j];
           j++;
           o++;
         }
	   }
	  else
		{
	  		collect[l].name[o]=person[i].name[j];
	  		o++;
	  		j++;
		}	
	}
	if(l==2)
 	{
 		collect[l].name[o]=0;
 		strrev(collect[l].name);
 	}
   if(l==0)    
 fprintf(vcf,";%s;;;\n",collect[l].name);
 else
 fprintf(vcf,"%s;%s;%s;;",collect[0].name,collect[2].name,collect[1].name);


fprintf(vcf,"\n");
 strrev(person[i].name);
 fprintf(vcf,"FN:%s\n",person[i].name);
 fprintf(vcf,"TEL;TYPE=Phone-1:%s\n",person[i].phone1);
 fprintf(vcf,"TEL;TYPE=Phone-2:%s\n",person[i].phone2);
 fprintf(vcf,"TEL;TYPE=Phone-3:%s\n",person[i].phone3);
 fprintf(vcf,"EMAIL;TYPE=WORK:%s\n",person[i].email);
 if(i==(n-1))
fprintf(vcf,"END:VCARD");
else fprintf(vcf,"END:VCARD\n");
} 
fclose(vcf);
return 1;   
}

int main()
{
  genvcf(4);
  return 0;
}