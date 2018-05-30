class Board:
    def __init__(self):
        self.Post_list = []
        self.Max_size = 10
    def Append_post(self,post):
        if len(self.Post_list) < self.Max_size:
            post.idx = len(self.Post_list)
            self.Post_list.append(post)
        else:
            print("작성개수 초과")
    def num(self):
        print("게시판 총 게시글 개수:",len(self.Post_list))
    def num_post(self, post_num):
        for i in range(len(self.Post_list)):
            if self.Post_list[i].idx == post_num:
                print("작성자:", self.Post_list[i].writer)
                print(self.Post_list[i].text)
    def writer_post(self, post_writer):
        for i in range(len(self.Post_list)):
            if self.Post_list[i].writer == post_writer:
                print(self.Post_list[i].text)
class Post:
    def __init__(self):
        self.idx = -1
        self.writer = ''
        self.text = ''
    def return_text(self):
        return self.text
    def write(self,input_text,writer):
        self.writer = writer
        self.text = input_text
    def return_writer(self,input_writer):
        return self.writer
Bord1 = Board()
post1 = Post()
post1.write("helloword!",'iruem')
post2 = Post()
post2.write("heeeeeellloooo",'IREEEEUUM')
Bord1.Append_post(post1)
Bord1.Append_post(post2)
Bord1.num()
Bord1.writer_post('iruem')