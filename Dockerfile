FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install --production

COPY . .

# УДАЛИ BOM из index.js если есть
RUN sed -i '1s/^\xEF\xBB\xBF//' index.js || true

EXPOSE 3000

CMD ["npm", "start"]
