o
    �`$eq  �                   @   s   d Z ddlZdd� ZdS )z\
Module to estimate the time required for a given daily task described in natural language.
�    Nc                 C   s0   d| v rd| v rt t�d| ��� �}|d S dS )z�
    Estimates time for a given daily task in natural language.
    
    Example: "Reading a 20-page book" might give 40 minutes, assuming an average of 
    2 minutes per page.
    �readZpagez\d+�   N)�int�re�search�group)�taskZpages� r	   �#/workspaces/Aihub/src/daily_task.py�estimate_time   s   r   )�__doc__r   r   r	   r	   r	   r
   �<module>   s    