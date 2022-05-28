import tkinter


# 윈도우 화면 초기화  
def windowInit() -> tkinter.Tk:
    root = tkinter.Tk()
    root.geometry('800x500')
    root.title('Stock Management')

    return root


# 메인  
if __name__ == '__main__':
    root = windowInit()

    # 왼쪽 프레임  
    frameleft = tkinter.Frame(root)
    frameleft.pack(side='left')

    # 버튼  
    buttonShowList = tkinter.Button(frameleft, text='Show All List')
    buttonSearch = tkinter.Button(frameleft, text='Search Data')
    buttonQuit = tkinter.Button(frameleft, text='Exit Programm')

    # 스크롤 바 
    yscroll = tkinter.Scrollbar(root)
    xscroll = tkinter.Scrollbar(root, orient='horizontal')
    yscroll.pack(side='right', fill='y')
    xscroll.pack(side='bottom', fill='x')

    # 텍스트 ( 데이터 보여주는 부분 )
    textShowData = tkinter.Listbox(root, height=80, yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
    yscroll.config(command=textShowData.yview)
    xscroll.config(command=textShowData.xview)

    # 붙여넣기 부분  
    buttonShowList.pack(side='top', fill='x', padx=10, pady=10)
    buttonSearch.pack(side='top', fill='x', padx=10, pady=10)
    buttonQuit.pack(side='bottom', fill='x', padx=10, pady=10)
    textShowData.pack(anchor='center', fill='both')

    root.mainloop()
