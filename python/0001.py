try:
    print('123\n123\n222\n5')
    pass
except ValueError:
    print('錯誤-類別:轉型錯誤，例如 int("abc")')
except TypeError:
    print('錯誤-類別:類型錯誤，例如數字加字串：1 + "2"')
except ZeroDivisionError:
    print('錯誤-類別:除以零')
except IndexError:
    print('錯誤-類別:索引超出範圍')
except KeyError:
    print('錯誤-類別:找不到鍵')
except FileNotFoundError:
    print('錯誤-類別:找不到檔案')
except PermissionError:
    print('錯誤-類別:沒有權限打開檔案')
except ImportError:
    print('錯誤-類別:模組載入失敗')
except AttributeError:
    print('錯誤-類別:沒有這個屬性或方法')
except NameError:
    print('錯誤-類別:使用未定義的變數')
except Exception as a:
    print('錯誤-類別:其他',a)