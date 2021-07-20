import ybc_funny as funny
import ybc_box as box
import random as r

res = box.buttonbox('请选择你的心河',['笑话','绕口令','脑筋急转弯','彩蛋？'])



if res == '笑话':
    funny_res_0 = funny.xiaohua()
    box.msgbox(funny_res_0)
elif res == '绕口令':
    funny_res_1 = funny.raokouling()
    box.msgbox(funny_res_1)
elif res == '脑筋急转弯':
    funny_res_2_ques = funny.jizhuanwan_question()
    funny_res_2_ques_answer = box.enterbox(funny_res_2_ques+'\n输入答案:')
    funny_res_2_answer = funny.jizhuanwan_answer(funny_res_2_ques)
    if '答案：'+funny_res_2_answer == funny_res_2_ques_answer:
        box.msgbox('猜对了！')
    else:
        box.msgbox('错了...')
        box.msgbox(funny_res_2_answer)
elif res == '彩蛋？':
    list_res = ['歇后语','谜语']
    funny_res_3_ranres = r.randint(0,1)
    box.msgbox('恭喜你！抽中了{}！'.format(list_res[funny_res_3_ranres]))
    if funny_res_3_ranres == 1:
        funny_res_3_1_ques = funny.miyu_question()
        funny_res_3_1_ques_answer = box.enterbox(funny_res_3_1_ques+'\n输入答案:')
        funny_res_3_1_answer = funny.miyu_answer(funny_res_3_1_ques)
        if funny_res_3_1_answer == '答案：'+funny_res_3_1_ques_answer:
            box.msgbox('猜对了！{}'.format(funny_res_3_1_answer))
        else:
            box.msgbox('错了...')
            box.msgbox(funny_res_3_1_answer)
    elif funny_res_3_ranres == 0:
        funny_res_3_0_ques = funny.xiehouyu_question()
        funny_res_3_0_ques_answer = box.enterbox(funny_res_3_0_ques+'\n输入答案:')
        funny_res_3_0_answer = funny.xiehouyu_answer(funny_res_3_0_ques)
        if funny_res_3_0_answer == '答案：'+funny_res_3_0_ques_answer:
            box.msgbox('猜对了！{}'.format(funny_res_3_0_answer))
        else:
            box.msgbox('错了...')
            box.msgbox(funny_res_3_0_answer)
