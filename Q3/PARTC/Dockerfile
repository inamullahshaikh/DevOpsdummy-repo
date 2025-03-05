FROM node:16  

WORKDIR /app  

COPY package.json .  
RUN npm install  

COPY . .  

# Ensure logs are written to a persistent directory
VOLUME [ "/app/logs" ]  

EXPOSE 3000  

CMD ["node", "index.js"]
