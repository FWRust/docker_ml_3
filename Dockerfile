FROM python:3.11

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-get install git-lfs
RUN git lfs install
RUN git clone https://huggingface.co/DFofanov78/rugpt3small_based_on_gpt2
RUN git lfs uninstall

EXPOSE 8000
CMD ["python3", "/app/main.py"]